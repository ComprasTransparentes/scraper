class CreateOrderItems < ActiveRecord::Migration
  def change
    create_table :order_items do |t|
      t.integer :correlativo
      t.integer :codigo_categoria
      t.string  :categoria
      t.integer :codigo_producto
      t.string  :producto
      t.string  :especificacion_comprador
      t.string  :especificacion_proveedor
      t.integer :cantidad
      t.string  :moneda
      t.integer :precio_neto
      t.integer :total_cargos
      t.integer :total_descuentos
      t.integer :total_impuestos
      t.integer :total
      t.timestamps null: false
    end
  end
end
