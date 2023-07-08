import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Box,
  Flex,
  Heading,
  Stack,
  FormControl,
  FormLabel,
  Input,
  Checkbox,
  Button,
  Wrap,
  WrapItem,
  Text,
  Badge,
  Alert,
  AlertIcon,
  CloseButton,
} from "@chakra-ui/react";

const App = () => {
  const [menu, setMenu] = useState([]);
  const [Name, setName] = useState("");
  const [dish_ids, setDishIds] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    price: "",
    availability: false,
  });
  const [orders, setOrders] = useState([]);
  const [successAlert, setSuccessAlert] = useState("");
  const [errorAlert, setErrorAlert] = useState("");

  const fetchMenu = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/menu");
      setMenu(response.data);
    } catch (error) {
      console.error("Error fetching menu:", error);
    }
  };

  const fetchOrders = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/orders");
      setOrders(response.data);
    } catch (error) {
      console.error("Error fetching orders:", error);
    }
  };

  useEffect(() => {
    fetchMenu();
    fetchOrders();
  }, []);

  const handleFormChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleCreateItem = async (e) => {
    e.preventDefault();
    let obj = formData;
    try {
      let response = await axios.post("http://127.0.0.1:5000/add_dish", obj);
      setSuccessAlert(response.data);
      fetchMenu();
      setFormData({
        name: "",
        price: "",
        availability: false,
      });
    } catch (error) {
      console.error("Error creating item:", error);
      setErrorAlert("Error creating item. Please try again.");
    }
  };

  const handleDeleteItem = async (id) => {
    try {
      let response = await axios.delete(
        `http://127.0.0.1:5000/remove_dish/${id}`
      );
      setSuccessAlert(response.data);
      fetchMenu();
    } catch (error) {
      console.error("Error deleting item:", error);
      setErrorAlert("Error deleting item. Please try again.");
    }
  };

  const handleUpdateAvailability = async (id, availability) => {
    try {
      let response = await axios.patch(
        `http://127.0.0.1:5000/update_availability/${id}`,
        {
          availability,
        }
      );
      setSuccessAlert(response.data);
      fetchMenu();
    } catch (error) {
      console.error("Error updating availability:", error);
      setErrorAlert("Error updating availability. Please try again.");
    }
  };

  const handleNewOrder = async () => {
    if (Name.length === 0) {
      setErrorAlert("Please enter a name.");
      return;
    }
    if (dish_ids.length === 0) {
      setErrorAlert("Please select at least one dish.");
      return;
    }
    try {
      const data = {
        customer_name: Name,
        dish_ids: dish_ids,
      };
      let response = await axios.post("http://127.0.0.1:5000/new_order", data);
      if (response.data === "Error: Invalid dish ID or dish not available") {
        setErrorAlert(response.data);
      } else {
        setSuccessAlert(response.data);
      }
      fetchOrders();
    } catch (error) {
      console.error("Error placing order:", error);
      setErrorAlert("Error placing order. Please try again.");
    }
    setName("");
    setDishIds([]);
  };

  const handleUpdateOrderStatus = async (orderId, newStatus) => {
    try {
      let response = await axios.post(
        `http://127.0.0.1:5000/update_order_status/${orderId}`,
        {
          status: newStatus,
        }
      );
      setSuccessAlert(response.data);
      fetchOrders();
    } catch (error) {
      console.error("Error updating order status:", error);
      setErrorAlert("Error updating order status. Please try again.");
    }
  };

  return (
    <Box p={8}>
      <Heading as="h1" mb={8}>
        Menu
      </Heading>

      <form onSubmit={handleCreateItem} className="form">
        <Stack direction="row" spacing={4} mb={4}>
          <FormControl>
            <FormLabel>Name:</FormLabel>
            <Input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleFormChange}
              required
            />
          </FormControl>

          <FormControl>
            <FormLabel>Price:</FormLabel>
            <Input
              type="number"
              step="0.01"
              name="price"
              value={formData.price}
              onChange={handleFormChange}
              required
            />
          </FormControl>

          <FormControl>
            <FormLabel>Availability:</FormLabel>
            <Checkbox
              name="availability"
              isChecked={formData.availability}
              onChange={handleFormChange}
            >
              Available
            </Checkbox>
          </FormControl>
        </Stack>

        <Button type="submit" colorScheme="blue" mb={4}>
          Create
        </Button>
      </form>

      <Heading as="h2" size="lg" mb={4}>
        Menu
      </Heading>
      <Wrap spacing={4} mb={8}>
        {menu.map((item) => (
          <WrapItem key={item._id} >
            <Box
              p={4}
              borderWidth="1px"
              borderRadius="md"
              boxShadow="sm"
              bg="white"
              overflow="hidden"
            >
              <Text fontWeight="bold">ID: {item._id}</Text>
              <Text>Name: {item.name}</Text>
              <Text>Price: {item.price}</Text>
              <Flex align="center" mt={2}>
                <Badge colorScheme={item.availability ? "green" : "red"}>
                  {item.availability ? "Available" : "Not available"}
                </Badge>
              </Flex>
              <Flex justify="space-between" mt={4}>
                <Button
                  onClick={() =>
                    handleUpdateAvailability(item._id, !item.availability)
                  }
                  size="sm"
                  variant="outline"
                  colorScheme={item.availability ? "green" : "red"}
                >
                  Toggle Availability
                </Button>
                <Button
                  onClick={() => handleDeleteItem(item._id)}
                  size="sm"
                  variant="outline"
                  colorScheme="red"
                >
                  Delete
                </Button>
                <Button
                  onClick={() => {
                    setDishIds([...dish_ids, item._id]);
                    setSuccessAlert("Dish selected");
                  }}
                  size="sm"
                  colorScheme="blue"
                >
                  Add to Order
                </Button>
              </Flex>
            </Box>
          </WrapItem>
        ))}
      </Wrap>

      <Heading as="h2" size="lg" mb={4}>
        Orders
      </Heading>
      {successAlert && (
        <Alert status="success" mb={4} rounded="md">
          <AlertIcon />
          {successAlert}
          <CloseButton
            ml="auto"
            onClick={() => setSuccessAlert("")}
            position="relative"
            top="-2px"
          />
        </Alert>
      )}
      {errorAlert && (
        <Alert status="error" mb={4} rounded="md">
          <AlertIcon />
          {errorAlert}
          <CloseButton
            ml="auto"
            onClick={() => setErrorAlert("")}
            position="relative"
            top="-2px"
          />
        </Alert>
      )}
      <FormControl>
        <FormLabel>Customer Name:</FormLabel>
        <Input
          type="text"
          value={Name}
          onChange={(e) => setName(e.target.value)}
          mb={4}
        />
      </FormControl>
      <Button
        onClick={handleNewOrder}
        colorScheme="blue"
        mb={4}
        disabled={dish_ids.length === 0}
      >
        Place Order
      </Button>
      <Wrap spacing={4}>
        {orders.map((order) => (
          <WrapItem key={order.id} w="300px">
            <Box
              p={4}
              borderWidth="1px"
              borderRadius="md"
              boxShadow="sm"
              bg="white"
              overflow="hidden"
            >
              <Text fontWeight="bold">Order ID: {order.id}</Text>
              <Text>Customer: {order.customer_name}</Text>
              <Text>Dishes-Ids: {order.dish_ids.join(", ")}</Text>
              <Text>Status: {order.status}</Text>
              {order.status !== "completed" && (
                <Button
                  onClick={() => handleUpdateOrderStatus(order._id, "completed")}
                  size="sm"
                  colorScheme="blue"
                  mt={2}
                >
                  Complete
                </Button>
              )}
            </Box>
          </WrapItem>
        ))}
      </Wrap>
    </Box>
  );
};

export default App;
