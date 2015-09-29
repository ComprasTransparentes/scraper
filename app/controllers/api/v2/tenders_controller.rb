class Api::V2::TendersController < Api::V2::ApiController
  def index
    @tenders = Tender.all.paginate(page: params[:page],per_page: params[:per_page])
    render json: @tenders, status: :ok
  end

  def show
    @tender = Tender.find(params[:id])
    render json: @tender
  end

  def search_by_code
    @tender = Tender.where(code: params[:code]).first
    render json: @tender
  end

end