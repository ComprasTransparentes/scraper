class AddStateToAdjudication < ActiveRecord::Migration
  def change
    add_column :adjudications, :state, :integer, default: 0
  end
end
