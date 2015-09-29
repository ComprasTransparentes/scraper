class CreateAdjudications < ActiveRecord::Migration
  def change
    create_table :adjudications do |t|
      t.string  :fecha
      t.string  :numero
      t.integer :numero_oferentes
      t.integer :tipo
      t.string  :url_acta
      t.integer :tender_id
      t.timestamps null: false
    end
  end
end
