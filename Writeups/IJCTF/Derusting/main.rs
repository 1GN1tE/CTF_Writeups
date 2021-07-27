use rand::SeedableRng;
use rand::rngs::StdRng;
use rand::seq::SliceRandom;
use std::str;

// Dependency rand = "*"

fn main() {
    let data = [0x42, 0x43, 0x24, 0x35, 0x7b, 0x7f, 0x0c, 0x68, 0x7d, 0x24, 0x24, 0x56, 0x49, 0x5e, 0x29, 0x3d, 0x29, 0x04, 0x57, 0x37, 0x3a, 0x6d, 0x33, 0x42, 0x3c, 0x0b, 0x4d, 0x11, 0x38, 0x6d, 0x4c, 0x29, 0x54, 0x7d, 0x64, 0x5a, 0x65, 0x2f, 0x24, 0x28];
    const sz: usize = 40; // data.len()

    for a in 0..256 {
        let mut rng = StdRng::seed_from_u64(a);
        let mut order_db = Vec::new();
        let mut mapp_db = Vec::new();

        let mut order = Vec::new();
        let mut mapp = Vec::new();

        for i in 0..data.len() {
            order.push(i);
            mapp.push(i);
        }

        for _ in 0..data.len() {
            order.shuffle(&mut rng);
            mapp.shuffle(&mut rng);
            order_db.push(order.clone());
            mapp_db.push(mapp.clone());
        }

        let mut buffer = data.clone();

        for _ in 0..data.len() {
            let ord = order_db.pop().unwrap();
            let mp = mapp_db.pop().unwrap();

            let mut tmp_buff = [0; sz];

            for i in 0..data.len() {
                tmp_buff[mp[i]] = buffer[i];
            }

            let mx = *ord.iter().max_by(|x, y| x.cmp(y)).unwrap();
            let index = ord.iter().position(|&r| r == mx).unwrap();
            let mut tmp_dec = [0; sz];
            tmp_dec[data.len() - 1] = tmp_buff[data.len() - 1];

            for i in (0..index).rev() {
                tmp_dec[ord[i]] = tmp_buff[i] ^ tmp_dec[ord[i + 1]];
            }
            for i in (index+1)..data.len() {
                tmp_dec[ord[i]] = tmp_buff[i - 1] ^ tmp_dec[ord[i - 1]];
            }
            buffer = tmp_dec.clone();
        }
        let flag =  str::from_utf8(&buffer).unwrap();
        if flag.starts_with("IJCTF") { 
            println!("{}",flag);
            break;
        }
    }
    /*
    order.shuffle(&mut rng);
    mapp.shuffle(&mut rng);
    println!("{:x?}", order);
    println!("{:x?}", mapp);

    for x in 0..(st.len() - 1) {
        ans.push(st[order[x]] ^ st[order[x+1]]);
    }
    ans.push(st[st.len() - 1]);

    for x in 0..st.len() {
        sol.push(ans[mapp[x]])
    }
    st = ans.clone();

    println!("{:x?}", ans);
    println!("{:x?}", sol);
    */
}
