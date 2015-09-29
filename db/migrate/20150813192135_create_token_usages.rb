class CreateTokenUsages < ActiveRecord::Migration
  def change
    create_table :token_usages do |t|
      t.integer    :token_id
      t.boolean    :active
      t.datetime   :last_used
      t.integer    :amount
      t.timestamps null: false
    end
  end
end
