module example.com/o2_hello

go 1.22.5

replace example.com/greetings => ../o1_greetings

require example.com/greetings v0.0.0-00010101000000-000000000000
