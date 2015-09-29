class CreateOrderDates < ActiveRecord::Migration
  def change
    create_table :order_dates do |t|
      t.string :fecha_creacion
      t.string :fecha_envio
      t.string :fecha_aceptacion
      t.string :fecha_cancelacion
      t.string :fecha_ultima_modificacion
      t.timestamps null: false
    end
  end
end
