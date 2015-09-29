class CreateTenderItems < ActiveRecord::Migration
  def change
    create_table :tender_items do |t|
      t.integer :correlativo
      t.integer :codigo_producto
      t.string  :codigo_categoria
      t.string  :categoria
      t.string  :nombre_producto
      t.string  :descripcion
      t.string  :unidad_medida
      t.integer :cantidad
      t.integer :tender_id
      t.string  :adjudicacion
      t.timestamps null: false
    end
  end
end
