class TenderParticipant < ActiveRecord::Base
  belongs_to :tender_item
  belongs_to :company
end
