Rails.application.routes.draw do
  # Angular App
  root to: 'home#index'
  # Api for insertions
  namespace :api do
    namespace :v1 do 
      resources :tenders do 
        collection do 
          get  :search
          post :state
          get  :search_for_participants
          post :create_participants
          get  :all
        end
      end
      resources :orders
      # Tokens
      resources :tokens do 
        collection do
          get  :get_token
          post :update_token
        end
      end
    end
  end
  namespace :api do
    namespace :v2 do
      resources :tenders
      resources :orders
    end
  end

# WEB APP ROUTES
  resources :home do 
    collection do
      get :search
      get :searchresults
      get :filesviewer
    end
  end

  match '*unmatched_route', :to => 'application#raise_not_found!', :via => :all
end
