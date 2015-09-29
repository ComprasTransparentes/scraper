class AddTenderIdToTenderParticipant < ActiveRecord::Migration
  def change
    add_column :tender_participants, :tender_id, :integer
  end
end
