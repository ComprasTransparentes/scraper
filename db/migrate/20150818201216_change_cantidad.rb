class ChangeCantidad < ActiveRecord::Migration
  def change
    change_column :tender_items, :cantidad, :float
  end
end
