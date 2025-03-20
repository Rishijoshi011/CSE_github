<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="Practical_6.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="lb_email_id" runat="server" Text="Enter Email Id:"></asp:Label>
            <asp:TextBox ID="inp_email_id" runat="server"></asp:TextBox>
            <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ErrorMessage="Email Id is required" ControlToValidate="inp_email_id" ForeColor="Red" Display="Dynamic"> </asp:RequiredFieldValidator>
            <asp:RegularExpressionValidator ID="RegularExpressionValidator1" runat="server" ErrorMessage="Invalid email format" ControlToValidate="inp_email_id" ValidationExpression="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" ForeColor="Red" Display="Dynamic"> </asp:RegularExpressionValidator>
            <br />
            <asp:Label ID="lb_password" runat="server" Text="Enter Password"></asp:Label>
            <asp:TextBox ID="inp_password" runat="server"></asp:TextBox>
            <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ErrorMessage="Password is Required" ControlToValidate="inp_password" ForeColor="Red" Display="Dynamic"> </asp:RequiredFieldValidator>
            <br />
            <asp:Label ID="lb_con_pass" runat="server" Text="Confirm Password"></asp:Label>
            <asp:TextBox ID="inp_con_pass" runat="server"></asp:TextBox>
            <asp:RequiredFieldValidator ID="RequiredFieldValidator3" runat="server" ErrorMessage="Password is Required" ControlToValidate="inp_con_pass" ForeColor="Red" Display="Dynamic"> </asp:RequiredFieldValidator>
            <asp:CompareValidator ID="CompareValidator1" runat="server" ErrorMessage="Passwords are not same" ControlToCompare="inp_con_pass" ControlToValidate="inp_password" ForeColor="Red" Display="Dynamic"></asp:CompareValidator>
            <br />
            <asp:Label ID="lb_age" runat="server" Text="Enter Age"></asp:Label>
            <asp:TextBox ID="inp_age" runat="server"></asp:TextBox>
            <asp:RequiredFieldValidator ID="RequiredFieldValidator4" runat="server" ErrorMessage="Age is Required" Display="Dynamic" ControlToValidate="inp_age" ForeColor="Red"> </asp:RequiredFieldValidator>
            <asp:RangeValidator ID="RangeValidator1" runat="server" ErrorMessage="Age should be between 18 to 26" Display="Dynamic" ControlToValidate="inp_age" MaximumValue="26"
                MinimumValue="18" ForeColor="Red"> </asp:RangeValidator>
            <br />
            <asp:Label ID="lb_user_id" runat="server" Text="Enter User Id"></asp:Label>
            <asp:TextBox ID="inp_user_id" runat="server"></asp:TextBox>
            <asp:RequiredFieldValidator ID="RequiredFieldValidator5" runat="server"  ErrorMessage="User id is Required" ControlToValidate="inp_user_id" ForeColor="Red" Display="Dynamic"></asp:RequiredFieldValidator>
            <asp:CustomValidator ID="CustomValidator1" runat="server" ErrorMessage="Ensure proper format (UID000000)" BorderStyle="None" ControlToValidate="inp_user_id" OnServerValidate="CustomValidator1_ServerValidate" ForeColor="Red" Display="Dynamic"> </asp:CustomValidator>  
            <br />
            <asp:Button ID="Button1" runat="server" Text="Submit" OnClick="Button1_Click" />
            <br />
            <asp:ValidationSummary ID="ValidationSummary1" runat="server" ForeColor="Red" ShowSummary="true" DisplayMode="List" />
            <br/>
            <asp:Label ID="lb_result" runat="server" Text=""></asp:Label>
        </div>
    </form>
</body>
</html>
