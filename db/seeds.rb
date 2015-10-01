# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
#
tokens = ['F8537A18-6766-4DEF-9E59-426B4FEE2844']
tokens.each do |t|
  Token.create(token: t)
end
