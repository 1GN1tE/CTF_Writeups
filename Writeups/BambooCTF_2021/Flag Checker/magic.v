module magic(
  input clk,
  input rst,
  input[7:0] inp,
  input[1:0] val,
  output reg[7:0] res
);
  always @(*) begin
    case (val)
      2'b00: res = (inp >> 3) | (inp << 5);
      2'b01: res = (inp << 2) | (inp >> 6);
      2'b10: res = inp + 8'b110111;
      2'b11: res = inp ^ 8'd55;
    endcase
  end
endmodule
