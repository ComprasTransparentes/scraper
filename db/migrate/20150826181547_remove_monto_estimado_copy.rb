class RemoveMontoEstimadoCopy < ActiveRecord::Migration
  def change
    remove_column :tenders, :monto_estimado_copy
  end
end
