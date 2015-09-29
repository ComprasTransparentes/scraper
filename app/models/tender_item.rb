class TenderItem < ActiveRecord::Base
  belongs_to :tender
  has_one :adjudication_item, :dependent => :destroy
  has_many :participants, class_name: "TenderParticipant", :dependent => :destroy
end
