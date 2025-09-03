fn main() {
    let mut a = [1, 2, 3, 4, 5];
    let i = 6; // 越界的索引
    let result = a.split_at_mut_checked(i);
}
