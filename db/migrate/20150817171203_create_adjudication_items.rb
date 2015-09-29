class CreateAdjudicationItems < ActiveRecord::Migration
  def change
    create_table :adjudication_items do |t|
      t.string     :cantidad
      t.string     :monto_unitario
      t.integer    :tender_item_id
      t.integer    :company_id
      t.timestamps null: false
    end
  end
end
