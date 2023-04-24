import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var list: [Int] = []
    for i in 0...n-1 {
        list.append(num_list[i])
    }
    return list
}