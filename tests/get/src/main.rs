fn main() {
    let mut a = [1, 2, 3, 4, 5];
    let mut i = 0;
    while i < 5 {
        a[i] = i;
        i = i + 1;
    }
    let result = a.get(i);
    // println!("{}", a[i]);
}
