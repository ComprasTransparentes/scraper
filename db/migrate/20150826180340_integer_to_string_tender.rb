class IntegerToStringTender < ActiveRecord::Migration
  def change
    change_column :tenders, :monto_estimado, :string
  end
end
