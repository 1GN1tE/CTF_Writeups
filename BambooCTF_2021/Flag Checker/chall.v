`include "./magic.v"

module chall(
  input clk,
  input rst,
  input[7:0] inp,
  output reg[7:0] res
);
  wire[1:0] val0 = inp[1:0];
  wire[1:0] val1 = inp[3:2];
  wire[1:0] val2 = inp[5:4];
  wire[1:0] val3 = inp[7:6];
  wire[7:0] res0, res1, res2, res3;

  magic m0(.clk(clk), .rst(rst), .inp(inp), .val(val0), .res(res0));
  magic m1(.clk(clk), .rst(rst), .inp(res0), .val(val1), .res(res1));
  magic m2(.clk(clk), .rst(rst), .inp(res1), .val(val2), .res(res2));
  magic m3(.clk(clk), .rst(rst), .inp(res2), .val(val3), .res(res3));

  always @(posedge clk) begin
    if (rst) begin
      assign res = inp;
    end else begin
      assign res = res3;
    end
  end
endmodule
