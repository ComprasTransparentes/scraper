class CreateCompanies < ActiveRecord::Migration
  def change
    create_table :companies do |t|
      t.string :code
      t.string :nombre
      t.string :actividad
      t.string :codigo_sucursal
      t.string :nombre_sucursal
      t.string :rut_sucursal
      t.string :direccion
      t.string :comuna
      t.string :region
      t.string :pais
      t.string :nombre_contacto
      t.string :cargo_contacto
      t.string :fono_contacto
      t.string :mail_contacto
      t.timestamps null: false
    end
  end
end
