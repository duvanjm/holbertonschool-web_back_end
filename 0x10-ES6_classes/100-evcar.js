import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(Car);
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this._range = range;
  }

  // eslint-disable-next-line class-methods-use-this
  cloneCar() {
    return new Car();
  }
}
