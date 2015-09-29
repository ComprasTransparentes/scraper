class CreateOrders < ActiveRecord::Migration
  def change
    create_table :orders do |t|
      t.string  :codigo
      t.string  :nombre
      t.integer :codigo_estado
      t.string  :estado
      t.string  :codigo_licitacion
      t.string  :descripcion
      t.string  :codigo_tipo
      t.string  :tipo
      t.string  :tipo_moneda
      t.integer :codigo_estado_proveedor
      t.string  :estado_proveedor
      t.string  :tiene_items
      t.integer :promedio_calificacion
      t.integer :cantidad_evaluacion
      t.integer :descuentos
      t.integer :cargos
      t.integer :total_neto
      t.integer :porcentaje_iva
      t.integer :impuestos
      t.integer :total
      t.string  :financiamiento
      t.string  :pais
      t.string  :tipo_despacho
      t.string  :forma_pago
      t.integer :buyer_id
      t.integer :provider_id
      t.timestamps null: false
    end
  end
end
