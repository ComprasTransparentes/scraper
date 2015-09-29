class CreateTransactionalOffers < ActiveRecord::Migration
  def change
    create_table :transactional_offers do |t|
      t.integer   :company_id
      t.integer   :tender_item_id
      t.integer   :offer_amount
      t.timestamps null: false
    end
  end
end
