class Token < ActiveRecord::Base
  has_many :token_usages
end
