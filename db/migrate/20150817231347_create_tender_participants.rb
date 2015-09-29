class CreateTenderParticipants < ActiveRecord::Migration
  def change
    create_table :tender_participants do |t|
      t.integer   :tender_item_id
      t.integer   :company_id
      t.boolean   :is_winner
      t.string    :price
      t.string    :part_valor
      t.string    :part_cant
      t.timestamps null: false
    end
  end
end
