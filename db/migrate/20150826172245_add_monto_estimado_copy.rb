class AddMontoEstimadoCopy < ActiveRecord::Migration
  def change
    add_column :tenders, :monto_estimado_copy, :string
  end
end
