###
#
#  Sort int arguments in asc
#
###

result = []
ARGV.each do |arg|
  # if not int, skip
  next if arg !~ /^-?[0-9]+$/

  # convert arg to int
  i_arg = arg.to_i

  # insert the result in postion
  is_inserted = false
  i = 0
  l = result.size
  while !is_inserted && i < l do
    if result[i] < i_arg
      i += 1
    else
      # correction
      result.insert(i, i_arg)
      is_inserted = true
      break
    end
  end
  result << i_arg if !is_inserted
end

puts result
