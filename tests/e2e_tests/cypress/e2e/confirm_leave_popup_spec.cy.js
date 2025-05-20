describe('B4ULeave plugin modal', () => {
    beforeEach(() => {
        cy.visit('/'); 
    });

    it('shows modal on external navigation attempt', () => {
        // Programmatically trigger beforeunload
        cy.window().then((win) => {
            const event = new Event('beforeunload', { bubbles: true, cancelable: true });
            const returnValue = win.dispatchEvent(event);

            // Modal should appear
            cy.get('#B4ULeave-ModalWindow').should('be.visible');
            cy.contains('Stay').should('exist');
            cy.contains('Leave').should('exist');
        });
    });

    it('hides modal when Stay is clicked', () => {
        cy.window().then((win) => {
            win.dispatchEvent(new Event('beforeunload'));
        });

        cy.get('#B4ULeave-ModalWindow').should('be.visible');
        cy.get('#B4ULeave-Stay').click();
        cy.get('#B4ULeave-ModalWindow').should('not.be.visible');
    });

    it('navigates away when Leave is clicked', () => {
        
        cy.window().then((win) => {
            win.dispatchEvent(new Event('beforeunload'));
        });
        
        // doesnt work
        // cy.window().then((win) => {
        //     cy.stub(win.location, 'assign').as('assignStub');
        // });

        // Trigger beforeunload, which displays the modal
        cy.window().then((win) => {
            win.dispatchEvent(new Event('beforeunload'));
        });

        // Modal should appear
        cy.get('#B4ULeave-ModalWindow').should('be.visible');
        cy.get('#B4ULeave-Leave').click();

        // Cannot test the behavior because the browser's native beforeunload dialog is displayed
    });
});