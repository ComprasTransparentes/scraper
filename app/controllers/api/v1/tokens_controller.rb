class Api::V1::TokensController < Api::ApiController

  def get_token
    @tokens = Token.all
    render json: {tokens:@tokens.pluck(:token)}, status: :ok
  end

  def update_token
    @token = Token.where(token: params[:token]).first
    @token.token_usages << TokenUsage.new(amount: params[:amount])
    render nothing: true, status: :ok
  end

end
