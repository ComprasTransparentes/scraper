class Tender < ActiveRecord::Base
  belongs_to :public_company, class_name: "PublicCompany", foreign_key: "buyer_id"
  has_one    :adjudication
  has_one    :date, class_name: "TenderDate", :dependent => :destroy
  has_many   :orders, :dependent => :destroy
  has_many   :states, class_name: "TenderState", :dependent => :destroy
  has_many   :items, class_name: "TenderItem", :dependent => :destroy

  # Add Items
  def add_items(items)
    if not items.blank? || items.nil?
      items.each do |item|
        adjudication_params = item[:adjudicacion]
        if adjudication_params != nil
          company = Company.where(rut_sucursal: adjudication_params[:rut_proveedor]).first
          if not company
            company = Company.create(rut_sucursal: adjudication_params[:rut_proveedor],nombre: adjudication_params[:nombre_proveedor])
          end
          item.permit!
          tender_item = TenderItem.new(item)
          self.items << tender_item
          AdjudicationItem.create(tender_item: tender_item, 
                                  company: company,
                                  monto_unitario: adjudication_params[:monto_unitario],
                                  cantidad: adjudication_params[:cantidad])
        else
          item.permit!
          self.items << TenderItem.new(item)
        end
      end
    end
  end

end
