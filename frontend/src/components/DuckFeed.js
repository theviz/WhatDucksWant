import { Component } from "react";
import axios from "axios";
import Select from "react-select";
import DuckLogo from "../assets/duck.png";
import CreatableSelect from "react-select/creatable";
import DatePicker from "react-datepicker";
import Switch from "react-switch";

export default class DuckFeed extends Component {
  constructor(props) {
    super(props);

    const axiosInstance = axios.create({
      baseURL: "https://cors-anywhere.herokuapp.com/http://34.125.181.24:5000/"
    });

    axiosInstance.interceptors.request.use(
      function(config) {
          config.headers["origin"] = "http://34.125.181.24:5000/"
          return config;
      },
    );

    this.api = axiosInstance;
    this.state = {
      isSaving: false,
      FoodTypeOptions: [],
      FoodType: null,
      FoodItem: null,
      Date: new Date(),
      repeat: false
    };
  }

  async componentDidMount() {
    const foodType = await this.api.get("/food-type");
    const foodItem = await this.api.get("/food-item");

    this.setState({
      FoodTypeOptions: foodType.data.map(type => ({
        label: type.name,
        value: type.name
      })),
      FoodItemOptions: foodItem.data.map(type => ({
        label: type.item_name,
        value: type.item_name
      }))
    });
  }

  isEmpty = value => {
    return value == null || value.trim() === "";
  };

  handleSubmit = async event => {
    event.preventDefault();
    if (this.isEmpty(this.state.FoodType)) {
      alert("Please select a value for Food Type");
      return;
    } else if (this.isEmpty(this.state.FoodItem)) {
      alert("Please select a value for Food Item");
      return;
    }

    try {
      this.setState({
        isSaving: true
      });
      const { ParkName, DucksCount, FoodAmount, Location } = event.target;
      const data = {
        name: ParkName.value,
        count: parseInt(DucksCount.value),
        at: new Date(this.state.Date).getTime(),
        location: Location.value,
        item_name: this.state.FoodItem,
        food_type: this.state.FoodType,
        food_amount: parseInt(FoodAmount.value),
        repeat: this.state.repeat
      };
      await this.api.post("/duck-food", data);
    } catch (error) {
      console.log(error);
    } finally {
      this.setState({
        isSaving: false
      });
    }
  };

  export = async () => {
    const csv = await this.api.get("/duck-food");
    var hiddenExportElement = document.createElement("a");
    hiddenExportElement.href =
      "data:text/csv;charset=utf-8," + encodeURI(csv.data);
    hiddenExportElement.target = "_blank";
    hiddenExportElement.download = "duck-feeds.csv";
    hiddenExportElement.click();
  };

  handleFoodTypeChange = (
    newValue: OnChangeValue<Any, false>,
    actionMeta: ActionMeta<Any>
  ) => {
    this.setState({
      FoodType: newValue.value
    });
  };

  handleFoodItemChange = (
    newValue: OnChangeValue<Any, false>,
    actionMeta: ActionMeta<Any>
  ) => {
    this.setState({
      FoodItem: newValue.value
    });
  };

  setDate = date => {
    this.setState({
      Date: date
    });
  };

  handleRepeatChange = checked => {
    this.setState({ repeat: checked });
  };

  render() {
    return (
      <div className="page-wrapper p-t-45 p-b-50">
        <div className="wrapper wrapper--w960">
          <div className="row card-5 br-0">
            <div className="col-3 p-0">
              <div className="navbar">
                <div className="logo">
                  <img src={DuckLogo} width="80px" alt="logo" />
                  <h4>Quack Quack...</h4>
                </div>
              </div>
            </div>
            <div className="col-9 p-0">
              <div className="card">
                <div className="card-body">
                  <div className="card-heading">
                    <h2 className="title">
                      What Do ducks eat?
                      <button
                        type="button"
                        className="download"
                        onClick={this.export}
                      >
                        {" "}
                        <i className="fa fa-download" aria-hidden="true"></i>
                      </button>
                    </h2>
                  </div>
                  <form id="feed-form" onSubmit={this.handleSubmit}>
                    <div className="form-row">
                      <div className="name">Park Name</div>
                      <div className="value">
                        <div className="input-group">
                          <input
                            className="input--style-5"
                            type="text"
                            name="ParkName"
                            required
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">No. of Ducks</div>
                      <div className="value">
                        <div className="input-group">
                          <input
                            className="input--style-5"
                            type="number"
                            name="DucksCount"
                            min="1"
                            required
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Food Type</div>
                      <div className="value">
                        <div className="input-group">
                          <CreatableSelect
                            options={this.state.FoodTypeOptions}
                            onChange={this.handleFoodTypeChange}
                            name="type"
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Food Item</div>
                      <div className="value">
                        <div className="input-group">
                          <Select
                            onChange={this.handleFoodItemChange}
                            options={this.state.FoodItemOptions}
                            name="FoodItem"
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Food Amount</div>
                      <div className="value">
                        <div className="input-group">
                          <input
                            className="input--style-5"
                            type="number"
                            name="FoodAmount"
                            min="1"
                            required
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row ">
                      <div className="name">Date</div>
                      <div className="value">
                        <div className="input-group">
                          <DatePicker
                            selected={this.state.Date}
                            onChange={date => this.setDate(date)}
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Location</div>
                      <div className="value">
                        <div className="input-group">
                          <input
                            className="input--style-5"
                            type="text"
                            name="Location"
                            placeholder="Halifax"
                            required
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Save as Default</div>
                      <div className="value">
                        <div className="input-group">
                          <Switch
                            onChange={this.handleRepeatChange}
                            checked={this.state.repeat}
                          />
                        </div>
                      </div>
                    </div>
                    <div style={{ textAlign: "center" }}>
                      <button
                        className="btn btn--radius-2 btn--red"
                        type="submit"
                        disabled={this.state.isSaving}
                      >
                        {this.state.isSaving ? "Feeding.." : "Feed"}
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
