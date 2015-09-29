# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
#   
tokens = ['564D2E7A-F342-45DC-8C3D-CBC7A9B2B27C','DA2A0390-CEAC-4B8D-AE14-A13BB8768EAE','4B291235-9246-46D7-B30F-A968B9E1018B','704B969C-9B3D-48CB-B5EC-1C5B5D1AF360','56EFE130-0555-41C3-8E79-E9ACC3A9E1BD','0942223B-FAE2-4060-950E-36D16916F7E2','404303EF-0694-475A-B091-02A419258262','33BDB1DA-7488-4FA4-B854-E47FD9EB9E5A','B0BC899A-C7C3-4252-B07C-FBFE2C35107C','B5B396EB-A59B-455D-AF8C-6ABECF1A8D5A']
tokens.each do |t|
  Token.create(token: t)
end