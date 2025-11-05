fn main() {
    // ##### Variables and Mutability
    let w = 3;  // Immutable
    let mut x = 5;  // Mutable
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");

    // ##### Constants
    const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
    println!("THREE HOURS IN SECONDS: {THREE_HOURS_IN_SECONDS}");

    // ##### Shadowing
    let a = 5;
    let a = a + 1;
    {
        let a = a * 2;
        println!("The value of a in the inner scope is: {a}");
    }
    println!("The value of a in the inner scope is: {a}");
}
