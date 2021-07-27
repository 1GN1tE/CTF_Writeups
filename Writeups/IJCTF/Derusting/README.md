# Derusting

Attachments:
* [Rusty](./Rusty)
* [enc](./enc)

## Solution
We are given a non stripped rust binary with debug info.

### Main
```rs
  v47 = 1;
  alloc::string::String::new::h26cbae42190ec72e(&v24);
  core::fmt::Arguments::new_v1::h0fc67a543e5c2de0( &v25,
    (___str_)__PAIR128__(1LL, &pieces),(__core::fmt::ArgumentV1_)(unsigned __int64)&::args);
  std::io::stdio::_print::h7e18c69e87ebeedb();
  std::io::stdio::stdin::h16158c407816830d();
  v26 = v0;
  std::io::stdio::Stdin::read_line::h54390211f5a91731();
  core::result::Result$LT$T$C$E$GT$::unwrap::h3ee37f0092e497c2(v21);
  v1 = _$LT$alloc..string..String$u20$as$u20$core..ops..deref..Deref$GT$::deref::h7972e8d5fc20fd7a((_str *)&v24, &self);
  v3.data_ptr = (u8 *)core::str::_$LT$impl$u20$str$GT$::trim::hbc62524cca89a5c1(v1, (_str)__PAIR128__(v2, v2));
  v4 = (alloc::string::String *)v3.data_ptr;
  _$LT$str$u20$as$u20$alloc..string..ToString$GT$::to_string::hea5984cbed75a39a(&v27, v3);
  core::ptr::drop_in_place$LT$alloc..string..String$GT$::hdf8b539c56b2f308(&v24);
  v47 = 1;
  v24 = v27;
  v28 = alloc::string::String::len::h825e4f75a4a97ad8(&v24);
  if ( (v28 & 1) != 0 )
  {
    if ( v28 == -1LL )
      core::panicking::panic::h60569d8a39169222();
    ++v28;
    v4 = 0LL;
    alloc::string::String::push::hd81ead5e50b5f90a(&v24, 0);
  }
  alloc::vec::Vec$LT$T$GT$::new::h325b47b1b2910d0d(&order);
  alloc::vec::Vec$LT$T$GT$::new::h325b47b1b2910d0d(&mapp);
```
It reads a line from stdin, stores it in a String, trims it and apends a null byte to it if it's of odd length. Then it creates two vectors `order` and `mapp`.
```rs
  v5.data_ptr = (u8 *)_$LT$alloc..string..String$u20$as$u20$core..ops..deref..Deref$GT$::deref::h7972e8d5fc20fd7a((_str *)&v24, v4);
  v48 = Rusty::calc::h48670832fda01f62(v5);
  rand_core::SeedableRng::seed_from_u64::h2c7250795f6fca31(&v31, v48);
```
Then it passes our input String to `calc` function and uses the return value to seed `StdRng`.

### `calc`
```rs
  v12 = msg;
  result = 0LL;
  self = (unsigned __int8)core::str::_$LT$impl$u20$str$GT$::chars::h3da1a63845b4e159(
                            (core::str::iter::Chars *)msg.data_ptr,(_str)__PAIR128__(v1, msg.length));
  v3 = v2;
  v4 = self;
  v5 = _$LT$I$u20$as$u20$core..iter..traits..collect..IntoIterator$GT$::into_iter::h068d7099feaf87a7(*(core::str::iter::Chars *)(&v3 - 1));
  *(_QWORD *)v9[0].gap0 = *(_QWORD *)v5.iter._marker.gap0;
  v10 = v5.iter.end;
  while ( 1 )
  {
    v11 = (unsigned int)_$LT$core..str..iter..Chars$u20$as$u20$core..iter..traits..iterator..Iterator$GT$::next::h4898ee8c1ff7a481(v9,v3);
    if ( v11 == 0x110000 )
      break;
    v13 = v11;
    v14 = v11;
    v15 = v11;
    result ^= v11;
  }
  return result;
```
It just creates a iterator of the chars of the string passed and calculates xor of all the chars and returns the value.

```rs
  v32.start = 0LL;
  v32.end = v28;
  v6.start = 0LL;
  v6.end = v28;
  v7 = _$LT$I$u20$as$u20$core..iter..traits..collect..IntoIterator$GT$::into_iter::h0344c52cd17b88e4(v6);
  v8 = (core::ops::range::Range<usize> *)v7.end;
  v33 = (core::option::Option<usize>)v7;
  while ( 1 )
  {
    v34 = core::iter::range::_$LT$impl$u20$core..iter..traits..iterator..Iterator$u20$for$u20$core..ops..range..Range$LT$A$GT$$GT$::next::h2c2da34fbd385412(&v33,v8);
    value = v9;
    if ( !v34 )
      break;
    v23 = value;
    v49 = value;
    v50 = value;
    v51 = value;
    alloc::vec::Vec$LT$T$C$A$GT$::push::hd2abd1f52a384ae7(&order, value);
    v8 = (core::ops::range::Range<usize> *)v23;
    alloc::vec::Vec$LT$T$C$A$GT$::push::hd2abd1f52a384ae7(&mapp, v23);
  }
```

Then it creates a iterator in range of `0 - len(input)` and pushes the iterator value into both the vectors `order` and `mmap`.

```rs
  v36.start = 0LL;
  v36.end = v28;
  v10.start = 0LL;
  v10.end = v28;
  v11 = _$LT$I$u20$as$u20$core..iter..traits..collect..IntoIterator$GT$::into_iter::h0344c52cd17b88e4(v10);
  v12 = (core::ops::range::Range<usize> *)v11.end;
  v37 = (core::option::Option<usize>)v11;
  while ( 1 )
  {
    v38 = core::iter::range::_$LT$impl$u20$core..iter..traits..iterator..Iterator$u20$for$u20$core..ops..range..Range$LT$A$GT$$GT$::next::h2c2da34fbd385412(&v37, v12);
    v39 = v13;
    if ( !v38 )
      break;
    v52 = v39;
    v53 = v39;
    v14.data_ptr = (usize *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..deref..DerefMut$GT$::deref_mut::h4a850e000ded5fcd(
                              (_mut__usize_ *)&order, v13);
    v15 = v14;
    _$LT$$u5b$T$u5d$$u20$as$u20$rand..seq..SliceRandom$GT$::shuffle::h6a3e01373570013f(v14, &v31);
    v16.data_ptr = (usize *)_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..deref..DerefMut$GT$::deref_mut::h4a850e000ded5fcd((_mut__usize_ *)&mapp,
                              (alloc::vec::Vec<usize,alloc::alloc::Global> *)v15.length);
    v17 = v16;
    _$LT$$u5b$T$u5d$$u20$as$u20$rand..seq..SliceRandom$GT$::shuffle::h6a3e01373570013f(v16, &v31);
    v18.data_ptr = (u8 *)_$LT$alloc..string..String$u20$as$u20$core..ops..deref..Deref$GT$::deref::h7972e8d5fc20fd7a(
                           (_str *)&v24, (alloc::string::String *)v17.length);
    Rusty::enc_map::h8722407589b4dfed(&v41, v18, &order, &mapp);
    v12 = (core::ops::range::Range<usize> *)&v41;
    _$LT$alloc..string..String$u20$as$u20$alloc..string..ToString$GT$::to_string::hf4f1d05914e6c8b4(&v40, &v41);
    core::ptr::drop_in_place$LT$alloc..string..String$GT$::hdf8b539c56b2f308(&v24);
    v47 = 1;
    v24 = v40;
    core::ptr::drop_in_place$LT$alloc..string..String$GT$::hdf8b539c56b2f308(&v41);
  }
```
It agains creates a iterator in range of `0 - len(input)`. It shuffles both the vectors and passes the input and the vectors to `enc_map` func. The output of the function replaces the input string.

```rs
  v47 = 0;
  v46 = v24;
  hex::encode::hb7e9ca658d4af18e(&v45, v22);
  v44 = (core::fmt::ArgumentV1 *)&v45;
  v54 = &v45;
  args.data_ptr = core::fmt::ArgumentV1::new::h97477eba8d05eb9a(
                    (core::fmt::ArgumentV1 *)&v45,
                    (alloc::string::String *)_$LT$alloc..string..String$u20$as$u20$core..fmt..Display$GT$::fmt::hbde356f78b2091fd,
                    v19);
  args.length = v20;
  core::fmt::Arguments::new_v1::h0fc67a543e5c2de0(
    &v42,
    (___str_)__PAIR128__(2LL, &stru_9B720),
    (__core::fmt::ArgumentV1_)__PAIR128__(1LL, &args));
  std::io::stdio::_print::h7e18c69e87ebeedb();
```
Then it hex encodes the encrypted string and prints it.

### `enc_map`
```rs
  v35.start = 0LL;
  v35.end = v27 - 1;
  v5.start = 0LL;
  v5.end = v27 - 1;
  v6 = _$LT$I$u20$as$u20$core..iter..traits..collect..IntoIterator$GT$::into_iter::h0344c52cd17b88e4(v5);
  v7 = v6.end;
  v36 = (core::option::Option<usize>)v6;
  while ( 1 )
  {
    v37 = core::iter::range::_$LT$impl$u20$core..iter..traits..iterator..Iterator$u20$for$u20$core..ops..range..Range$LT$A$GT$$GT$::next::h2c2da34fbd385412(
            &v36,
            (core::ops::range::Range<usize> *)v7);
    index = v8;
    if ( !v37 )
      break;
    v24 = index;
    v49 = index;
    v50 = index;
    v51 = index;
    v25 = _$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::h20305dde976ac687(
            order,
            index);
    if ( *v25 >= v31 )
      core::panicking::panic_bounds_check::hab5cb3227e3c0b2e();
    v23 = self[*v25];
    if ( v24 == -1LL )
      core::panicking::panic::h60569d8a39169222();
    v22 = *_$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::h20305dde976ac687(
             order,
             v24 + 1);
    if ( v22 >= v31 )
      core::panicking::panic_bounds_check::hab5cb3227e3c0b2e();
    v7 = (unsigned __int8)(self[v22] ^ v23);
    alloc::string::String::push::hd81ead5e50b5f90a(&v34, v7);
  }
```
It creates some Strings, then it iterates over `0 - len(input) - 1`. It xores `input[order[i]]` and `input[order[i+1]]` and pushes the reuslt in a String.
```rs
  v9.length = v31;
  v9.data_ptr = self;
  v26 = core::slice::_$LT$impl$u20$$u5b$T$u5d$$GT$::len::hf174ceb3f6e0c94d(v9);
  v21 = v26 - 1;
  if ( !v26 )
    core::panicking::panic::h60569d8a39169222();
  if ( v21 >= v31 )
    core::panicking::panic_bounds_check::hab5cb3227e3c0b2e();
  alloc::string::String::push::hd81ead5e50b5f90a(&v34, self[v21]);
```
Then it pushes the last element of the input in the String of xored values.
```rs
  v10.length = v31;
  v10.data_ptr = self;
  v20 = core::slice::_$LT$impl$u20$$u5b$T$u5d$$GT$::len::hf174ceb3f6e0c94d(v10);
  v39.start = 0LL;
  v39.end = v20;
  v10.data_ptr = 0LL;
  v10.length = v20;
  v11 = _$LT$I$u20$as$u20$core..iter..traits..collect..IntoIterator$GT$::into_iter::h0344c52cd17b88e4((core::ops::range::Range<usize>)v10);
  v12 = v11.end;
  v40 = (core::option::Option<usize>)v11;
  while ( 1 )
  {
    v41 = core::iter::range::_$LT$impl$u20$core..iter..traits..iterator..Iterator$u20$for$u20$core..ops..range..Range$LT$A$GT$$GT$::next::h2c2da34fbd385412(
            &v40, (core::ops::range::Range<usize> *)v12);
    v42 = v13;
    if ( !v41 )
      break;
    v19 = (__int64)v42;
    v52 = v42;
    v53 = v42;
    v54 = v42;
    v16 = alloc::string::String::as_bytes::hda31620cfadc9bfd((__u8_ *)&v34, v13);
    v17 = v14;
    v18 = _$LT$alloc..vec..Vec$LT$T$C$A$GT$$u20$as$u20$core..ops..index..Index$LT$I$GT$$GT$::index::h20305dde976ac687(
            mapp,v19);
    if ( *v18 >= v17 )
      core::panicking::panic_bounds_check::hab5cb3227e3c0b2e();
    v12 = *((unsigned __int8 *)&v16->data_ptr + *v18);
    alloc::string::String::push::hd81ead5e50b5f90a(v32, v12);
  }
  core::ptr::drop_in_place$LT$alloc..string..String$GT$::hdf8b539c56b2f308(&v34);
```
Then it extractes values of input with the help of `mmap` and pushes it into a new string. `sol.push(ans[mapp[i]])`

### Decryption
- The seed of the rand is dependent on `calc`, as it xores chars the range will be `0 - 256` easy to bruteforce
- We can calculate all the shuffled values and start reversing from backwards, i.e. the last shuffled value
- The mmap can be easily reversed
- To reverse the xor, we know the last character of the input. So we can calculate the index of the highest value in order vector. The index will be of the last character. Using the index as a fixed point we can loop backwards and forwards xoring the values at index contained in `order` vector to get the original input.
- We bruteforce till we get a string starting with `IJCTF`

Solution script [here](./main.rs)

## Flag
> IJCTF{d45a51a84f2387e49c8f6d252f75ecad}
