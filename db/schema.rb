# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20150826181547) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "adjudication_items", force: :cascade do |t|
    t.string   "cantidad"
    t.string   "monto_unitario"
    t.integer  "tender_item_id"
    t.integer  "company_id"
    t.datetime "created_at",     null: false
    t.datetime "updated_at",     null: false
  end

  create_table "adjudications", force: :cascade do |t|
    t.string   "fecha"
    t.string   "numero"
    t.integer  "numero_oferentes"
    t.integer  "tipo"
    t.string   "url_acta"
    t.integer  "tender_id"
    t.datetime "created_at",                   null: false
    t.datetime "updated_at",                   null: false
    t.integer  "state",            default: 0
  end

  create_table "companies", force: :cascade do |t|
    t.string   "code"
    t.string   "nombre"
    t.string   "actividad"
    t.string   "codigo_sucursal"
    t.string   "nombre_sucursal"
    t.string   "rut_sucursal"
    t.string   "direccion"
    t.string   "comuna"
    t.string   "region"
    t.string   "pais"
    t.string   "nombre_contacto"
    t.string   "cargo_contacto"
    t.string   "fono_contacto"
    t.string   "mail_contacto"
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
  end

  create_table "order_dates", force: :cascade do |t|
    t.string   "fecha_creacion"
    t.string   "fecha_envio"
    t.string   "fecha_aceptacion"
    t.string   "fecha_cancelacion"
    t.string   "fecha_ultima_modificacion"
    t.datetime "created_at",                null: false
    t.datetime "updated_at",                null: false
  end

  create_table "order_items", force: :cascade do |t|
    t.integer  "correlativo"
    t.integer  "codigo_categoria"
    t.string   "categoria"
    t.integer  "codigo_producto"
    t.string   "producto"
    t.string   "especificacion_comprador"
    t.string   "especificacion_proveedor"
    t.integer  "cantidad"
    t.string   "moneda"
    t.integer  "precio_neto"
    t.integer  "total_cargos"
    t.integer  "total_descuentos"
    t.integer  "total_impuestos"
    t.integer  "total"
    t.datetime "created_at",               null: false
    t.datetime "updated_at",               null: false
  end

  create_table "orders", force: :cascade do |t|
    t.string   "codigo"
    t.string   "nombre"
    t.integer  "codigo_estado"
    t.string   "estado"
    t.string   "codigo_licitacion"
    t.string   "descripcion"
    t.string   "codigo_tipo"
    t.string   "tipo"
    t.string   "tipo_moneda"
    t.integer  "codigo_estado_proveedor"
    t.string   "estado_proveedor"
    t.string   "tiene_items"
    t.integer  "promedio_calificacion"
    t.integer  "cantidad_evaluacion"
    t.integer  "descuentos"
    t.integer  "cargos"
    t.integer  "total_neto"
    t.integer  "porcentaje_iva"
    t.integer  "impuestos"
    t.integer  "total"
    t.string   "financiamiento"
    t.string   "pais"
    t.string   "tipo_despacho"
    t.string   "forma_pago"
    t.integer  "buyer_id"
    t.integer  "provider_id"
    t.datetime "created_at",              null: false
    t.datetime "updated_at",              null: false
  end

  create_table "public_companies", force: :cascade do |t|
    t.string   "code"
    t.string   "nombre"
    t.string   "rut_unidad"
    t.string   "codigo_unidad"
    t.string   "nombre_unidad"
    t.string   "direccion_unidad"
    t.string   "comuna_unidad"
    t.string   "region_unidad"
    t.string   "rut_usuario"
    t.string   "codigo_usuario"
    t.string   "nombre_usuario"
    t.string   "cargo_usuario"
    t.datetime "created_at",       null: false
    t.datetime "updated_at",       null: false
  end

  create_table "tender_dates", force: :cascade do |t|
    t.string   "fecha_creacion"
    t.string   "fecha_cierre"
    t.string   "fecha_inicio"
    t.string   "fecha_final"
    t.string   "fecha_pub_respuestas"
    t.string   "fecha_acto_apertura_tecnica"
    t.string   "fecha_acto_apertura_economica"
    t.string   "fecha_publicacion"
    t.string   "fecha_adjudicacion"
    t.string   "fecha_estimada_adjudicacion"
    t.string   "fecha_soporte_fisico"
    t.string   "fecha_tiempo_evaluacion"
    t.string   "fecha_estimada_firma"
    t.string   "fechas_usuario"
    t.string   "fecha_visita_terreno"
    t.string   "fecha_entrega_antecedentes"
    t.integer  "tender_id"
    t.datetime "created_at",                    null: false
    t.datetime "updated_at",                    null: false
  end

  create_table "tender_items", force: :cascade do |t|
    t.integer  "correlativo"
    t.integer  "codigo_producto"
    t.string   "codigo_categoria"
    t.string   "categoria"
    t.string   "nombre_producto"
    t.string   "descripcion"
    t.string   "unidad_medida"
    t.float    "cantidad"
    t.integer  "tender_id"
    t.string   "adjudicacion"
    t.datetime "created_at",       null: false
    t.datetime "updated_at",       null: false
  end

  create_table "tender_participants", force: :cascade do |t|
    t.integer  "tender_item_id"
    t.integer  "company_id"
    t.boolean  "is_winner"
    t.string   "price"
    t.string   "part_valor"
    t.string   "part_cant"
    t.datetime "created_at",     null: false
    t.datetime "updated_at",     null: false
    t.integer  "tender_id"
  end

  create_table "tender_states", force: :cascade do |t|
    t.integer  "state"
    t.integer  "tender_id"
    t.string   "date"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "tenders", force: :cascade do |t|
    t.string   "code"
    t.text     "name"
    t.text     "descripcion"
    t.integer  "buyer_id"
    t.string   "dias_cierre_licitacion"
    t.integer  "informada"
    t.integer  "codigo_tipo"
    t.string   "tipo"
    t.string   "tipo_convocatoria"
    t.string   "moneda"
    t.integer  "etapas"
    t.string   "estado_etapas"
    t.string   "toma_razon"
    t.integer  "estado_publicidad_ofertas"
    t.string   "justificacion_publicidad"
    t.string   "contrato"
    t.string   "obras"
    t.integer  "cantidad_reclamos"
    t.integer  "unidad_tiempo_evaluacion"
    t.string   "direccion_visita"
    t.string   "direccion_entrega"
    t.integer  "estimacion"
    t.string   "fuente_financiamiento"
    t.integer  "visibilidad_monto"
    t.string   "monto_estimado"
    t.string   "tiempo"
    t.string   "unidad_tiempo"
    t.integer  "modalidad"
    t.string   "tipo_pago"
    t.string   "nombre_responsable_pago"
    t.string   "email_responsable_pago"
    t.string   "nombre_responsable_contrato"
    t.string   "email_responsable_contrato"
    t.string   "fono_responsable_contrato"
    t.string   "prohibicion_contratacion"
    t.string   "sub_contratacion"
    t.string   "unidad_tiempo_duracion_contrato"
    t.string   "tiempo_duracion_contrato"
    t.string   "tipo_duracion_contrato"
    t.string   "justificacion_monto_estimado"
    t.string   "observacion_contract"
    t.integer  "extension_plazo"
    t.integer  "es_base_tipo"
    t.string   "unidad_tiempo_contrato_licitacion"
    t.string   "valor_tiempo_renovacion"
    t.string   "periodo_tiempo_renovacion"
    t.integer  "es_renovable"
    t.integer  "adjudication_id"
    t.datetime "created_at",                        null: false
    t.datetime "updated_at",                        null: false
  end

  create_table "token_usages", force: :cascade do |t|
    t.integer  "token_id"
    t.boolean  "active"
    t.datetime "last_used"
    t.integer  "amount"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "tokens", force: :cascade do |t|
    t.string   "token"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "transactional_offers", force: :cascade do |t|
    t.integer  "company_id"
    t.integer  "tender_item_id"
    t.integer  "offer_amount"
    t.datetime "created_at",     null: false
    t.datetime "updated_at",     null: false
  end

end
