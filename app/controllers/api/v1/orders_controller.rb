class Api::V1::OrdersController < Api::ApiController
  before_action :set_order, except: [:index]
  
  # All Paginated
  def index
    @orders = Order.all.paginate(page: params[:page],per_page: params[:per_page])
    render json: @orders, status: :ok
  end

  # Insert in db
  def create
    if not @order
      order = Order.new(order_params)
      order.order_states << OrderState.new(state_params)
      if order.save
        render nothing: true, status: :created
      else
        render nothing: true,  status: :bad_request
      end
    else
      render nothing: true, status: :ok
    end
  end

  # Update state
  def update_state
    if @order.order_states << OrderState.new(state_params)
      render nothing: true, status: :ok
    else
      render nothing: true, status: :bad_request
    end
  end

  # Search by code
  def search
    if @order
      render json: @order
    else
      render nothing: true, status: :bad_request
    end
  end

  private

  def order_params
    params.permit(Order.column_names)
  end

  def state_params
    params.permit(:state)
  end

  def set_order
    @order = Order.where(code: order_params[:code]).first
  end

end
