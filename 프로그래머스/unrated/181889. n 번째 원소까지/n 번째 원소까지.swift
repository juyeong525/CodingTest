import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var list: [Int] = []
    for i in 0...n-1 {
        list.append(num_list[i])
    }
    // return Array(num_list[...(n-1)])
    // return Array(num_list.prefix(n))
    return list
}