class Api::V1::TendersController < Api::ApiController
  before_action :set_tender, except: [:index, :show, :all, :search_for_participants]

  # All Paginated
  def index
    @tenders = Tender.all.paginate(page: params[:page],per_page: params[:per_page])
    render json: @tenders, status: :ok
  end

  # Insert in db
  def create
    if not @tender
      tender = Tender.new(tender_params)
      # Assoicate Public Company
      tender.public_company = PublicCompany.new(company_params)
      # Add State to states array
      tender.states << TenderState.new(state_params)
      # Add Dates
      tender.date = TenderDate.new(date_params)
      # Add Items
      tender.add_items(params[:items]) if params[:items]
      # Adjudication 
      tender.adjudication =  Adjudication.new(adjudication_params) if adjudication_params
      
      if tender.save
        render nothing: true, status: :created
      else
        render nothing: true,  status: :server_error
      end
    
    else
      @tender.states << TenderState.new(state_params)
      render nothing: true, status: :bad_request
    end
  end

  # Update state
  def state
    if @tender.states << TenderState.new(state_params)
      render nothing: true, status: :ok
    else
      render nothing: true, status: :bad_request
    end
  end

  # Search by code
  def search
    if @tender
      states_object = @tender.states.order(:created_at).last
      if states_object
        render json: { isCreated: true, state: states_object.state }, status: :ok
      else
        render nothing: true, status: :server_error
      end
    else
      render json: { isCreated: false }, status: :not_found
    end
  end

  def search_for_participants
    @tender = Tender.find(params[:id])
    items = []
    @tender.items.each do |t|
      items << { item_id: t.id , descripcion: t.descripcion, cantidad: t.cantidad}
    end
    render json: {tender_id: @tender.id, 
                  url: @tender.adjudication.url_acta,
                  items: items
                 }
  end

  def all
    adjudications = Adjudication.where(state: 0).paginate(page: params[:page],per_page: params[:per_page])
    render json: adjudications
  end

  def create_participants
    @tender = Tender.find(params[:tender_id])
    @tender.adjudication.update(state: 1)
    params[:items].each do |i|
      i[:parts].each do |p|
        company = Company.where(rut_sucursal: p[:part_rut]).first
        if not company
          company = Company.create(rut_sucursal: p[:part_rut],nombre: p[:part_name])
        end
        TenderParticipant.create(tender_item_id: i[:item_id],
                                 is_winner: p[:is_winner],
                                 price: p[:part_precio],
                                 company: company,
                                 tender_id: @tender.id )
      end
    end
  end

  # Private Methods mostly params
  private
  def tender_params
    params.permit(Tender.column_names)
  end

  def state_params
    params.permit(:state, :date)
  end

  def adjudication_params
    params.require(:adjudicacion).permit(Adjudication.column_names) if params[:adjudicacion]
  end

  def date_params
    params.require(:fechas).permit! if params[:fechas]
  end

  def company_params
    params.require(:buyer).permit(PublicCompany.column_names) if params[:buyer]
  end

  def set_tender
    @tender = Tender.where(code: tender_params[:code]).first
  end
end
