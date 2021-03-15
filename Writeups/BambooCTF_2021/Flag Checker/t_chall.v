`timescale 1ns/10ps

`include "./chall.v"

module t_chall();
  reg clk, rst, ok;
  reg[7:0] inp, idx, tmp;
  reg[7:0] res[32:0];
  wire[7:0] out;
  wire[7:0] target[32:0], flag[32:0];

  assign {target[0], target[1], target[2], target[3], target[4], target[5], target[6], target[7], target[8], target[9], target[10], target[11], target[12], target[13], target[14], target[15], target[16], target[17], target[18], target[19], target[20], target[21], target[22], target[23], target[24], target[25], target[26], target[27], target[28], target[29], target[30], target[31]} = {8'd182, 8'd199, 8'd159, 8'd225, 8'd210, 8'd6, 8'd246, 8'd8, 8'd172, 8'd245, 8'd6, 8'd246, 8'd8, 8'd245, 8'd199, 8'd154, 8'd225, 8'd245, 8'd182, 8'd245, 8'd165, 8'd225, 8'd245, 8'd7, 8'd237, 8'd246, 8'd7, 8'd43, 8'd246, 8'd8, 8'd248, 8'd215};

  // change the content of the flag as you need
  assign flag[0] = 102;
  assign flag[1] = 108;
  assign flag[2] = 97;
  assign flag[3] = 103;
  assign flag[4] = 123;
  assign flag[5] = 116;
  assign flag[6] = 104;
  assign flag[7] = 105;
  assign flag[8] = 115;
  assign flag[9] = 95;
  assign flag[10] = 105;
  assign flag[11] = 115;
  assign flag[12] = 95;
  assign flag[13] = 102;
  assign flag[14] = 97;
  assign flag[15] = 107;
  assign flag[16] = 101;
  assign flag[17] = 95;
  assign flag[18] = 102;
  assign flag[19] = 97;
  assign flag[20] = 107;
  assign flag[21] = 101;
  assign flag[22] = 95;
  assign flag[23] = 102;
  assign flag[24] = 97;
  assign flag[25] = 107;
  assign flag[26] = 101;
  assign flag[27] = 95;
  assign flag[28] = 33;
  assign flag[29] = 33;
  assign flag[30] = 33;
  assign flag[31] = 125;

  chall ch(.clk(clk), .rst(rst), .inp(inp), .res(out));

  initial begin
    $dumpfile("chall.vcd");
    $dumpvars;

    clk = 1'b0;
    #1 rst = 1'b1;
    #1 rst = 1'b0;
    inp = flag[0];
    tmp = target[0];

    ok = 1'b1;
    for (idx = 0; idx < 32; idx++) begin
      inp = flag[idx];
      tmp = target[idx];
      #4;
    end

    if (ok) begin
      $display("ok");
    end else begin
      $display("no");
    end

    $finish;
  end

  always @(posedge clk) begin
    #1 ok = ok & (out == tmp);
  end

  always begin
    #2 clk = ~clk;
  end
endmodule
