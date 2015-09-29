class CreateTenderStates < ActiveRecord::Migration
  def change
    create_table :tender_states do |t|
      t.integer  :state
      t.integer  :tender_id
      t.string   :date
      t.timestamps null: false
    end
  end
end
