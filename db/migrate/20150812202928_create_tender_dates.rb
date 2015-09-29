class CreateTenderDates < ActiveRecord::Migration
  def change
    create_table :tender_dates do |t|
      t.string :fecha_creacion
      t.string :fecha_cierre
      t.string :fecha_inicio
      t.string :fecha_final
      t.string :fecha_pub_respuestas
      t.string :fecha_acto_apertura_tecnica
      t.string :fecha_acto_apertura_economica
      t.string :fecha_publicacion
      t.string :fecha_adjudicacion
      t.string :fecha_estimada_adjudicacion
      t.string :fecha_soporte_fisico
      t.string :fecha_tiempo_evaluacion
      t.string :fecha_estimada_firma
      t.string :fechas_usuario
      t.string :fecha_visita_terreno
      t.string :fecha_entrega_antecedentes
      t.integer :tender_id
      t.timestamps null: false
    end
  end
end
