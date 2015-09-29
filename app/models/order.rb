class Order < ActiveRecord::Base
  belongs_to :tender
  has_many   :order_items
  has_many   :order_dates
end
