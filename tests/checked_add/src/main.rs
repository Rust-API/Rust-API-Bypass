fn main() {
    
    // test checked_add with overflow
    let a:i128 = 34028236692093846346337460743176821144;
    let b:i128 = 8888888888888888888888888888888888888;
    let result:i128 = a.checked_add(b).unwrap();
    println!("result: {:?}", result);
}
