import { Component } from "react";
import axios from "axios";

export default class DuckFeed extends Component {
  constructor(props) {
    super(props);

    const axiosInstance = axios.create({
      baseURL:
        "https://node-express-env.eba-cth7sfse.us-east-1.elasticbeanstalk.com/"
    });

    this.api = axiosInstance;
    this.state = {
      isSaving: false
    };
  }

  componentDidMount() {
    /*==================================================================
            [ Daterangepicker ]*/
    try {
      $(".js-datepicker").daterangepicker({
        singleDatePicker: true,
        showDropdowns: true,
        autoUpdateInput: false,
        locale: {
          format: "DD/MM/YYYY"
        }
      });

      var myCalendar = $(".js-datepicker");
      var isClick = 0;

      $(window).on("click", function() {
        isClick = 0;
      });

      $(myCalendar).on("apply.daterangepicker", function(ev, picker) {
        isClick = 0;
        $(this).val(picker.startDate.format("DD/MM/YYYY"));
      });

      $(".js-btn-calendar").on("click", function(e) {
        e.stopPropagation();

        if (isClick === 1) isClick = 0;
        else if (isClick === 0) isClick = 1;

        if (isClick === 1) {
          myCalendar.focus();
        }
      });

      $(myCalendar).on("click", function(e) {
        e.stopPropagation();
        isClick = 1;
      });

      $(".daterangepicker").on("click", function(e) {
        e.stopPropagation();
      });
    } catch (er) {
      console.log(er);
    }
    /*[ Select 2 Config ]
            ===========================================================*/

    try {
      var selectSimple = $(".js-select-simple");

      selectSimple.each(function() {
        var that = $(this);
        var selectBox = that.find("select");
        var selectDropdown = that.find(".select-dropdown");
        selectBox.select2({
          dropdownParent: selectDropdown
        });
      });
    } catch (err) {
      console.log(err);
    }
  }

  handleSubmit = async event => {
    event.preventDefault();

    const {
      DucksCount,
      type,
      FoodItem,
      FoodAmount,
      Time,
      Location
    } = event.target;
    const data = {
      ducksCount: DucksCount.value,
      time: Time.value,
      location: Location.value,
      food: FoodItem.value,
      foodType: type.value,
      foodAmount: FoodAmount.value
    };

    await this.api.post("/feed", data);
  };

  render() {
    return (
      <div className="page-wrapper p-t-45 p-b-50">
        <div className="wrapper wrapper--w960">
          <div className="row card-5 br-0">
            <div className="col-3 p-0">
              <div className="navbar">
                <div className="logo">
                  <img src="images/logo.png" width="150px" alt="logo" />
                  <h5>Quack Quack...</h5>
                </div>
              </div>
            </div>
            <div className="col-9 p-0">
              <div className="card">
                <div className="card-body">
                  <div className="card-heading">
                    <h2 className="title">
                      What Do ducks eat?
                      <i className="fa fa-download" aria-hidden="true"></i>
                    </h2>
                  </div>
                  <form onSubmit={this.handleSubmit}>
                    <div className="form-row">
                      <div className="name">No. of Ducks</div>
                      <div className="value">
                        <div className="input-group">
                          <input
                            className="input--style-5"
                            type="text"
                            name="DucksCount"
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Food Type</div>
                      <div className="value">
                        <div className="input-group">
                          <div className="rs-select2 js-select-simple select--no-search">
                            <select name="type">
                              <option disabled="disabled">Choose option</option>
                              <option>Subject 1</option>
                              <option>Subject 2</option>
                              <option>Subject 3</option>
                            </select>
                            <div className="select-dropdown"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Food Item</div>
                      <div className="value">
                        <div className="input-group">
                          <div className="rs-select2 js-select-simple select--no-search">
                            <select name="FoodItem">
                              <option disabled="disabled">Choose option</option>
                              <option>Subject 1</option>
                              <option>Subject 2</option>
                              <option>Subject 3</option>
                            </select>
                            <div className="select-dropdown"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div className="form-row">
                      <div className="name">Food Amount</div>
                      <div className="value">
                        <div className="input-group">
                          <input
                            className="input--style-5"
                            type="text"
                            name="FoodAmount"
                          />
                        </div>
                      </div>
                    </div>
                    <div className="form-row m-b-55">
                      <div className="name">Time</div>
                      <div className="value">
                        <div className="row row-refine">
                          <div className="col-3">
                            <div className="input-group-desc">
                              <input
                                className="input--style-5"
                                type="text"
                                name="Time"
                              />
                              <label className="label--desc">Day</label>
                            </div>
                          </div>
                          <div className="col-3">
                            <div className="input-group-desc">
                              <input
                                className="input--style-5"
                                type="text"
                                name="phone"
                              />
                              <label className="label--desc">Month</label>
                            </div>
                          </div>
                          <div className="col-3">
                            <div className="input-group-desc">
                              <input
                                className="input--style-5"
                                type="text"
                                name="phone"
                              />
                              <label className="label--desc">Year</label>
                            </div>
                          </div>
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
