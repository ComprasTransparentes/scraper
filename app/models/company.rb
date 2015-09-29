class Company < ActiveRecord::Base
  has_many :adjudication_items
  has_many :tender_participants
end
