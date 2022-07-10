#!/usr/bin/env python3
"""Model for aircraft flights."""


from pprint import pprint as pp
from tkinter.messagebox import NO


class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        self._number = self._valid_number(number)
        self._aircraft = aircraft
        self._seating = self._build_seating(aircraft)

    def _valid_number(self, number):
        if len(number) != 5:
            raise ValueError("Invalid length of flight number '{}'".format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route number '{}'".format(number))
        return number

    def _build_seating(self, aircraft):
        if not aircraft:
            return
        rows, seats = aircraft.seating_plan()
        return [None] + [{letter: None for letter in seats} for _ in rows]

    def _parse_seat(self, seat):
        """Parse a seat into a valid row and letter.

        Args:
            seat: A seat designator such as '12C' or '21F'.

        Returns:
            A tuple contains an integer and a string for row number and seat letter.

        Raises:
            ValueError: If the seat is invalid.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def _passenger_seats(self):
        """An itrable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_passenger(self, seat, passenger):
        """Allocate a seat to a passanger.

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passange to a different seat.

        Args:
            from_seat: The existing seat designator for the
                       passanger to be moved.
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passanger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied")

        self._seating[to_row][to_letter], self._seating[from_row][from_letter] = (
            self._seating[from_row][from_letter],
            None,
        )

    def num_available_seats(self):
        return sum(
            sum(1 for seat in row.values() if seat is None)
            for row in self._seating
            if row is not None
        )

    def print_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}  Flight: {1}  Seat: {2}  Aircraft: {3} |".format(
        passenger, flight_number, seat, aircraft
    )
    border = "+" + "-" * (len(output) - 2) + "+"
    lines = [border, output, border]
    print("\n".join(lines))
    print()


def main():
    flight = Flight("SN060", None)
    print(flight.number(), flight.airline())

    aircraft = AirbusA319("G-EUPT")
    print(aircraft.registration(), aircraft.model(), aircraft.seating_plan())

    flight = Flight("BA750", AirbusA319("G-EUPT"))
    print(flight.aircraft_model())
    pp(flight._seating)

    flight.allocate_passenger("12A", "Guido van Rossum")
    flight.allocate_passenger("15F", "Bjarne Stroustrup")
    flight.allocate_passenger("15E", "Anders Hejlsberg")
    flight.allocate_passenger("1C", "John McCarthy")
    flight.allocate_passenger("1D", "Richard Hickey")
    pp(flight._seating)

    flight.relocate_passenger("12A", "15D")
    pp(flight._seating)

    print(flight.num_available_seats())

    flight.print_boarding_cards(console_card_printer)

    print(AirbusA319("").num_seats(), Boeing777("").num_seats())


if __name__ == "__main__":
    main()
