class CreatePublicCompanies < ActiveRecord::Migration
  def change
    create_table :public_companies do |t|
      t.string :code
      t.string :nombre
      t.string :rut_unidad
      t.string :codigo_unidad
      t.string :nombre_unidad
      t.string :direccion_unidad
      t.string :comuna_unidad
      t.string :region_unidad
      t.string :rut_usuario
      t.string :codigo_usuario
      t.string :nombre_usuario
      t.string :cargo_usuario
      t.timestamps null: false
    end
  end
end
