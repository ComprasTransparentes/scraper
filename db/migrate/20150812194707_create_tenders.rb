class CreateTenders < ActiveRecord::Migration
  def change
    create_table :tenders do |t|
      t.string  :code
      t.text    :name
      t.text    :descripcion
      t.integer :buyer_id
      t.string  :dias_cierre_licitacion
      t.integer :informada
      t.integer :codigo_tipo
      t.string  :tipo
      t.string  :tipo_convocatoria
      t.string  :moneda
      t.integer :etapas
      t.string  :estado_etapas
      t.string  :toma_razon
      t.integer :estado_publicidad_ofertas
      t.string  :justificacion_publicidad
      t.string  :contrato
      t.string  :obras
      t.integer :cantidad_reclamos
      t.integer :unidad_tiempo_evaluacion
      t.string  :direccion_visita
      t.string  :direccion_entrega
      t.integer :estimacion
      t.string  :fuente_financiamiento
      t.integer :visibilidad_monto
      t.integer :monto_estimado
      t.string  :tiempo
      t.string  :unidad_tiempo
      t.integer :modalidad
      t.string  :tipo_pago
      t.string  :nombre_responsable_pago
      t.string  :email_responsable_pago
      t.string  :nombre_responsable_contrato
      t.string  :email_responsable_contrato
      t.string  :fono_responsable_contrato
      t.string  :prohibicion_contratacion
      t.string  :sub_contratacion
      t.string  :unidad_tiempo_duracion_contrato
      t.string  :tiempo_duracion_contrato
      t.string  :tipo_duracion_contrato
      t.string  :justificacion_monto_estimado
      t.string  :observacion_contract
      t.integer :extension_plazo
      t.integer :es_base_tipo
      t.string  :unidad_tiempo_contrato_licitacion
      t.string  :valor_tiempo_renovacion
      t.string  :periodo_tiempo_renovacion
      t.integer :es_renovable
      t.integer :adjudication_id
      t.timestamps null: false
    end
  end
end
