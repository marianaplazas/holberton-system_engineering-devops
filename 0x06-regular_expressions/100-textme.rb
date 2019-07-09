#!/usr/bin/env ruby
#advance task
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
